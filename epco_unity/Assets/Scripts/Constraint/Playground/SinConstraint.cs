using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SinConstraint : MonoBehaviour, ConstraintInterface
{
    [SerializeField]
    protected string constraintId = "unnamed_sin";

    [SerializeField]
    protected Vector3 planarNormal = new Vector3();

    [SerializeField]
    protected Vector3 sinalNormal = new Vector3();

    [SerializeField]
    protected float planarBias = 0;

    [SerializeField]
    protected float sinalBias = 0;

    [SerializeField]
    protected float sinalScale = 1;

    public string GetConstraintType() {
        return "sin_constraint";
    } 

    public string GetId() {
        return this.constraintId;
    }

    public bool IsValid(Dictionary<string, DataStreamInterface> sources) {
        DataStreamInterface source = sources["sphere_position"];
        float[] data = source.GetData(0);
        Vector3 position = new Vector3(data[0], data[1], data[2]);
        
        float val = Vector3.Dot(this.planarNormal, position) +  (this.sinalScale * Mathf.Sin(Vector3.Dot(this.sinalNormal, position) + this.sinalBias)) + this.planarBias;
        //Debug.Log($"({position.x}, {position.z}) ({this.planarNormal.x}, {this.planarNormal.z}) {val}");
        if (val >= 0) {
            return false;
        }

        return true;
    }
}
