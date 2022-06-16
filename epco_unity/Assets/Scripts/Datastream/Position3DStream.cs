using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Position3DStream : MonoBehaviour, DataStreamInterface
{
    [SerializeField]
    protected string objectId = "unnamed_position3d";

    [SerializeField]
    protected Transform position = null;

    [SerializeField]
    protected List<float> lowerBounds = new List<float>();

    [SerializeField]
    protected List<float> upperBounds = new List<float>();

    protected float[] buffer = new float[3];

    public float[] GetData(float currentTime) {
        this.buffer[0] = this.transform.position.x;
        this.buffer[1] = this.transform.position.y;
        this.buffer[2] = this.transform.position.z;

        return this.buffer;
    }

    public void SetData(float[] data) {
        this.position.position = new Vector3(
            data[0],
            data[1],
            data[2]
        );
    }

    public string GetId() {
        return this.objectId;
    }

    public (List<float>, List<float>) GetBounds() {
        return (this.lowerBounds, this.upperBounds);
    }

    public int GetSize() {
        return 3;
    }

    public string GetStreamType() {
        return "position3d";
    }

    
}
