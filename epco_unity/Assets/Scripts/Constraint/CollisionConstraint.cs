using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CollisionConstraint : MonoBehaviour, ConstraintInterface {
    [SerializeField]
    protected string constraintId = "unnamed_collision";

    [SerializeField]
    protected Transform agent = null;

    public bool IsValid(Dictionary<string, DataStreamInterface> sources) {
        bool isCollision = Physics.CheckSphere(this.agent.position, this.agent.localScale.x / 2);

        return !isCollision;
    }

    public string GetId() {
        return this.constraintId;
    }

    public string GetConstraintType() {
        return "collision_constraint";
    }
}
