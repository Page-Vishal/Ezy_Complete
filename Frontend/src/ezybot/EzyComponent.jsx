// EzyComponent.jsx
import { useState } from "react";
import "./EzyComponent.css";
import ChatUI from "./ChatUI.jsx"

import botimage from "../assets/Ezy.png"
import chaticon from "../assets/chatbot.png"

export default function EzyBot() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="chatbot-container">
      {isOpen && (
        <>
        <div className="chatbot-card">
          <div className="chatbot-header">
            <img src={botimage} alt="Ezy Logo" className="chatbot-avatar" />
            <div>
              <div className="chatbot-title">Ezy</div>
              <div className="chatbot-subtitle">
                Ezy is a smart and friendly bot to assist you during RentNepal Session. 
              </div>
            </div>
          </div>
          <div className="chatbot">
            <div className="chat-history">
              <ChatUI />
            </div>
          </div>
        </div>
        </>
      )}

      <button className="chatbot-toggle" onClick={() => setIsOpen(!isOpen)}>
        <img src={chaticon} alt="Chat" />
      </button>
    </div>
  );
}
