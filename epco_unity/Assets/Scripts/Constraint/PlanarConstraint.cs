using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlanarConstraint : MonoBehaviour, ConstraintInterface
{
    [SerializeField]
    protected string constraintId = "unnamed_planar";

    [SerializeField]
    protected Vector3 normal = new Vector3();

    [SerializeField]
    protected float bias = 0;

    public string GetConstraintType() {
        return "planar";
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

        float val = (this.normal.x * x) + (this.normal.y * y) + (this.normal.z * z) + this.bias;

        if (val >= 0) {
            return false;
        }

        return true;
    }
}
