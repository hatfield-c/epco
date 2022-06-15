using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LinearConstraint : MonoBehaviour, ConstraintInterface
{
    [SerializeField]
    protected float upperBound = 1;

    public bool IsValid(Dictionary<string, DataStreamInterface> sources) {
        DataStreamInterface source = sources["function_sin"];

        return false;
    }
}
