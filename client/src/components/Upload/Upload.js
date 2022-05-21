import React from "react";
import ModalForm from "./ModalForm";
import { useState } from "react";

export default function Upload(onUpdate) {
  const [isOpen, setIsOpen] = useState(false);

  const openModel = () => {
    setIsOpen(true);
  };
  const closeModal = () => {
    setIsOpen(false);
  };

  return (
    <div>
      <nav className="navbar fixed-top navbar-expand-lg navbar-light bg-light">
        <button type="button" className="btn" onClick={openModel}>
          <svg
            width="1.5em"
            height="1.5em"
            style={{ marginRight: 10 + "px" }}
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            className="bi bi-plus-square"
            viewBox="0 0 16 16"
          >
            <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z" />
            <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z" />
          </svg>
        </button>
      </nav>
      {isOpen && (
        <ModalForm
          isOpen={isOpen}
          closeModal={closeModal}
          onUpdate={onUpdate}
        />
      )}
    </div>
  );
}
