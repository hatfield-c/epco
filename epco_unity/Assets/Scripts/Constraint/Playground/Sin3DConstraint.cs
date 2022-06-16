using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SinConstraint : MonoBehaviour, ConstraintInterface
{
    [SerializeField]
    protected string constraintId = "unnamed_sin3d";

    [SerializeField]
    protected float xScale = 1;

    [SerializeField]
    protected float zScale = 1;

    [SerializeField]
    protected float b = 1;

    public string GetConstraintType() {
        return "sin3d";
    }

    public string GetId() {
        return this.constraintId;
    }

    public bool IsValid(Dictionary<string, DataStreamInterface> sources) {
        DataStreamInterface source = sources["sphere_position"];
        float[] data = source.GetData(0);
        float x = data[0];
        float y = data[1];
        float z = data[2];

        float val = (this.xScale * x) + (this.zScale * z) + Mathf.Sin(x + z) + this.b - y;

        if(val >= 0) {
            return false;
        }

        return true;
    }
}
