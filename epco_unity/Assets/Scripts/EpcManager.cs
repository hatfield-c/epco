using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EpcManager : MonoBehaviour
{
    protected TcpManager tcpManager = null;

    public void Init(TcpManager tcpManager) {
        this.tcpManager = tcpManager;

        this.QueryEpc();
    }

    public void QueryEpc() {
        this.tcpManager.WriteMessage("From Unity: Test query");

        string response = this.tcpManager.ReadMessage();
        Debug.Log($"Python response: {response}");

    }
}
