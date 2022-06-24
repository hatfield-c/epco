using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SceneManager : MonoBehaviour
{
    [Header("References")]
    [SerializeField]
    protected StreamManager streamManager = null;

    [SerializeField]
    protected ConstraintManager constraintManager = null;

    [SerializeField]
    protected TrainGenerator trainGenerator = null;

    [SerializeField]
    protected TcpManager tcpManager = null;

    [SerializeField]
    protected EpcManager epcManager = null;

    void FixedUpdate() {
        //Debug.Log(
            //this.constraintManager.IsValid(this.streamManager.GetSources())
        //);
    }

    public void ActiveInference() {
        if (!Application.isPlaying) {
            Debug.LogError("Error: You must be in Play mode to enter Active Inference mode.");
            return;
        }

        this.tcpManager.Init();
        this.epcManager.Init(this.tcpManager);
    }

    public void RenderConstraintSpace() {
        if (!Application.isPlaying) {
            Debug.LogError("Error: You must be in Play mode to generate training data.");
            return;
        }

        this.constraintManager.RenderValidSpace(this.streamManager.GetSources());
    }

    public void GenerateTrainingData() {
        if (!Application.isPlaying) {
            Debug.LogError("Error: You must be in Play mode to generate training data.");
            return;
        }

        this.trainGenerator.GenerateData();
    }
}
