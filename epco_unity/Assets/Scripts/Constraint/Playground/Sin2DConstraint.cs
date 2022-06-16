using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Sin2DConstraint : MonoBehaviour, ConstraintInterface {
    [SerializeField]
    protected string constraintId = "unnamed_sin2d";

    [SerializeField]
    protected float xScale = 1;

    [SerializeField]
    protected float xSinScale = 1;

    [SerializeField]
    protected float b = 1;

    public string GetConstraintType() {
        return "sin2d";
    }

    public string GetId() {
        return this.constraintId;
    }

    public bool IsValid(Dictionary<string, DataStreamInterface> sources) {
        DataStreamInterface source = sources["sphere_position"];
        float[] data = source.GetData(0);
        float x = data[0];
        float z = data[1];

        float val = (this.xScale * x) + Mathf.Sin(this.xSinScale * x) + this.b - z;

        if(val >= 0) {
            return false;
        }

        return true;
    }
}
