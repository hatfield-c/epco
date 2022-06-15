using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(SceneManager))]
public class EditorTrainGenerator : Editor
{
    public override void OnInspectorGUI() {
        base.OnInspectorGUI();

        SceneManager trainGen = (SceneManager)this.target;

        if(GUILayout.Button("Generate Training Data")) {
            trainGen.GenerateTrainingData();
        }
    }
}
