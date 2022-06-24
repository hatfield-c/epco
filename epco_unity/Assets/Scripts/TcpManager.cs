using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.IO;

public class TcpManager : MonoBehaviour
{
    [SerializeField]
    protected string ipAddress = "localhost";

    [SerializeField]
    protected int toPythonPort = 0;

    [SerializeField]
    protected int toUnityPort = 0;

    [SerializeField]
    protected float timeout = 30;

    protected TcpClient unitySocket = null;
    protected TcpClient pythonSocket = null;

    protected NetworkStream writeStream = null;
    protected StreamReader readStream = null;
    protected NetworkStream readNetworkStream = null;

    public void Init() {
        Debug.Log("Init TCP");

        this.ConnectWrite();
        this.ConnectRead();
    }

    public void WriteMessage(string message) {
        if (this.unitySocket == null) {
            UnityEngine.Debug.LogError("No server connection was found. WriteMessage() aborted.");
        }

        try {
            if (this.writeStream.CanWrite) {
                byte[] encodedMessage = Encoding.ASCII.GetBytes(message + "\n");

                this.writeStream.Write(encodedMessage, 0, encodedMessage.Length);
            }
        } catch (System.Exception exception) {
            UnityEngine.Debug.Log(exception.StackTrace);
            UnityEngine.Debug.Log(exception.Message);
            UnityEngine.Debug.LogError("Exception thrown while trying to send message to Python. Discarding message.");
        }
    }

    public string ReadMessage() {
        string response = null;

        try {

            response = this.readStream.ReadLine();

        } catch (System.Exception exception) {
            UnityEngine.Debug.Log(exception);
            UnityEngine.Debug.LogError("\nException occured while trying to read from the Sumo Server.");
        }

        return response;
    }

    protected void ConnectWrite() {
        System.Diagnostics.Stopwatch connectionTimer = new System.Diagnostics.Stopwatch();
        connectionTimer.Start();

        bool attemptConnection = true;
        while (attemptConnection) {

            if (connectionTimer.ElapsedMilliseconds / 1000 < this.timeout) {
                this.pythonSocket = new TcpClient();
                this.pythonSocket.Connect(this.ipAddress, this.toPythonPort);
                this.writeStream = this.pythonSocket.GetStream();

                attemptConnection = false;
            } else {
                connectionTimer.Stop();
                UnityEngine.Debug.LogError("Connection timed out before an attempted connection was made by the server.");

                return;
            }
        }

        connectionTimer.Stop();
    }

    protected void ConnectRead() {
        System.Diagnostics.Stopwatch connectionTimer = new System.Diagnostics.Stopwatch();
        connectionTimer.Start();

        bool attemptConnection = true;
        while (attemptConnection) {

            if (connectionTimer.ElapsedMilliseconds / 1000 < this.timeout) {
                this.unitySocket = new TcpClient();
                this.unitySocket.Connect(this.ipAddress, this.toUnityPort);
                this.readNetworkStream = this.unitySocket.GetStream();
                this.readStream = new StreamReader(this.readNetworkStream);

                attemptConnection = false;
            } else {
                connectionTimer.Stop();
                UnityEngine.Debug.LogError("Connection timed out before an attempted connection was made by the server.");

                return;
            }
        }

        connectionTimer.Stop();
    }

}
