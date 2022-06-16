using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ConstraintManager : MonoBehaviour
{
    [SerializeField]
    protected List<GameObject> constraintObjects = new List<GameObject>();

    protected List<string> constraintIds = new List<string>();
    protected Dictionary<string, ConstraintInterface> constraints = new Dictionary<string, ConstraintInterface>();

    void Start() {
        ConstraintInterface constraint;
        string constraintId;

        for (int i = 0; i < this.constraintObjects.Count; i++) {
            constraint = this.constraintObjects[i].GetComponent<ConstraintInterface>();
            constraintId = constraint.GetId();

            this.constraintIds.Add(constraintId);
            this.constraints.Add(constraintId, constraint);
        }
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
}
