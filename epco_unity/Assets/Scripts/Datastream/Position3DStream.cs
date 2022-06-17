using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Position3DStream : MonoBehaviour, DataStreamInterface
{
    [SerializeField]
    protected string objectId = "unnamed_position3d";

    [SerializeField]
    protected Transform target = null;

    [SerializeField]
    protected List<float> lowerBounds = new List<float>();

    [SerializeField]
    protected List<float> upperBounds = new List<float>();

    protected List<List<float>> bounds = new List<List<float>>();
    protected float[] buffer = new float[3];

    void Start() {
        this.bounds.Add(this.lowerBounds);
        this.bounds.Add(this.upperBounds);
    }

    public float[] GetData(float currentTime) {
        this.buffer[0] = this.target.position.x;
        this.buffer[1] = this.target.position.y;
        this.buffer[2] = this.target.position.z;

        return this.buffer;
    }

    public void SetData(float[] data) {
        this.target.position = new Vector3(
            data[0],
            data[1],
            data[2]
        );
    }

    public string GetId() {
        return this.objectId;
    }

    public List<List<float>> GetBounds() {
        return this.bounds;
    }

    public int GetSize() {
        return 3;
    }

    public string GetStreamType() {
        return "position3d";
    }

    
}
