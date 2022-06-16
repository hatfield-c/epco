using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SceneManager : MonoBehaviour
{
    [SerializeField]
    protected StreamManager streamManager = null;

    [SerializeField]
    protected ConstraintManager constraintManager = null;

    [SerializeField]
    protected TrainGenerator trainGenerator = null;

    void FixedUpdate() {
        Debug.Log(
            this.constraintManager.IsValid(this.streamManager.GetSources())
        );
    }

    public void GenerateTrainingData() {
        this.trainGenerator.GenerateData();
    }
}
