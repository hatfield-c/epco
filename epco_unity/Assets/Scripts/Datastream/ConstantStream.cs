using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ConstantStream : MonoBehaviour, DataStreamInterface
{
    [SerializeField]
    protected string streamId = "unnamed_constant";

    [SerializeField]
    protected float[] data = null;

    [SerializeField]
    protected List<float> upperBounds = null;

    [SerializeField]
    protected List<float> lowerBounds = null;

    protected List<List<float>> bounds = new List<List<float>>();

    void Start() {
        this.bounds.Add(this.lowerBounds);
        this.bounds.Add(this.upperBounds);
    }

    public List<List<float>> GetBounds() {
        return this.bounds;
    }

    public int GetSize() {
        return this.data.Length;
    }

    public float[] GetData(float currentTime) {
        return this.data;
    }

    public void SetData(float[] data) {
        this.data = data;
    }

    public string GetStreamType() {
        return "constant";
    }

    public string GetId() {
        return this.streamId;
    }
}
