using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ConstraintManager : MonoBehaviour
{
    [SerializeField]
    protected List<ConstraintInterface> sources = new List<ConstraintInterface>();

    public bool IsValid(float[] sample) {
        return true;
    }

    void Start()
    {
        
    }

}
