using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Position2DStream : MonoBehaviour, DataStreamInterface {
    [SerializeField]
    protected string objectId = "unnamed_position2d";

    [SerializeField]
    protected Transform target = null;

    [SerializeField]
    protected List<float> lowerBounds = new List<float>();

    [SerializeField]
    protected List<float> upperBounds = new List<float>();

    protected float[] buffer = new float[2];

    public float[] GetData(float currentTime) {
        this.buffer[0] = this.target.position.x;
        this.buffer[1] = this.target.position.z;

        return this.buffer;
    }

    public void SetData(float[] data) {
        this.target.position = new Vector3(
            data[0],
            this.target.position.y,
            data[1]
       );
    }

    public string GetId() {
        return this.objectId;
    }

    public (List<float>, List<float>) GetBounds() {
        return (this.lowerBounds, this.upperBounds);
    }

    public int GetSize() {
        return 2;
    }

    public string GetStreamType() {
        return "position2d";
    }


}
