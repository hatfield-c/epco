using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ConstraintManager : MonoBehaviour
{
    [Header("References")]
    [SerializeField]
    protected List<GameObject> constraintObjects = new List<GameObject>();

    [Header("Render")]
    [SerializeField]
    protected GameObject prefab = null;

    [SerializeField]
    protected Vector3 prefabScale = new Vector3(1 ,1 ,1);

    [SerializeField]
    protected Vector3 granularity = new Vector3(1, 1, 1);

    [SerializeField]
    protected Vector3 lowerBounds = new Vector3(0, 0, 0);

    [SerializeField]
    protected Vector3 upperBounds = new Vector3(1, 1, 1);

    protected List<string> constraintIds = new List<string>();
    protected Dictionary<string, ConstraintInterface> constraints = new Dictionary<string, ConstraintInterface>();

    protected Vector3 renderStep = new Vector3();

    void Start() {
        ConstraintInterface constraint;
        string constraintId;

        for (int i = 0; i < this.constraintObjects.Count; i++) {
            constraint = this.constraintObjects[i].GetComponent<ConstraintInterface>();
            constraintId = constraint.GetId();

            this.constraintIds.Add(constraintId);
            this.constraints.Add(constraintId, constraint);
        }

        Vector3 diff = this.upperBounds - this.lowerBounds;
        this.renderStep = new Vector3(
            diff.x / this.granularity.x, 
            diff.y / this.granularity.y,
            diff.z / this.granularity.z
        );
    }

    public bool IsValid(Dictionary<string, DataStreamInterface> sources) {
        ConstraintInterface constraint;

        for(int i = 0; i < this.constraintIds.Count; i++) {
            string constraintId = this.constraintIds[i];
            constraint = this.constraints[constraintId];

            bool valid = constraint.IsValid(sources);

            if (!valid) {
                return false;
            }
        }

        return true;
    }

    public void RenderValidSpace(Dictionary<string, DataStreamInterface> sources) {
        DataStreamInterface source = sources["sphere_position"];
        float[] positionData = new float[3];

        GameObject container = new GameObject("render_container");

        for (float x = this.lowerBounds.x; x < this.upperBounds.x; x += this.renderStep.x) {
            for (float y = this.lowerBounds.y; y < this.upperBounds.y; y += this.renderStep.y) {
                for (float z = this.lowerBounds.z; z < this.upperBounds.z; z += this.renderStep.z) {
                    positionData[0] = x;
                    positionData[1] = y;
                    positionData[2] = z;

                    source.SetData(positionData);

                    bool isValid = this.IsValid(sources);
                    
                    if (!isValid) {
                        continue;
                    }

                    GameObject voxel = Instantiate(this.prefab);
                    
                    voxel.transform.localScale = new Vector3(
                        this.renderStep.x * this.prefabScale.x,
                        this.renderStep.y * this.prefabScale.y,
                        this.renderStep.z * this.prefabScale.z
                    );

                    voxel.transform.position = new Vector3(x, y, z);
                    voxel.transform.parent = container.transform;
                }
            }
        }
    }
}
