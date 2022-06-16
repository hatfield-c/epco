using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CollisionConstraint : MonoBehaviour, ConstraintInterface {
    [SerializeField]
    protected string constraintId = "unnamed_collision";

    [SerializeField]
    protected GameObject agent = null;

    protected bool isColliding = false;

    void OnTriggerEnter(Collider other) {
        if (other.gameObject == this.agent) {
            this.isColliding = true;
        }
    }

    void OnTriggerExit(Collider other) {
        if(other.gameObject == this.agent) {
            this.isColliding = false;
        }
    }

    public bool IsValid(Dictionary<string, DataStreamInterface> sources) {
        return this.isColliding;
    }

    public string GetId() {
        return this.constraintId;
    }

    public string GetConstraintType() {
        return "collision_constraint";
    }
}
