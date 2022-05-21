import Form from "react-bootstrap/Form";
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/button";
import { Component } from "react";
import axios from "../../utils/axios";
import toast, { Toaster } from "react-hot-toast";

export default class ModalForm extends Component {
  constructor(props) {
    super(props);
    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append("file", this.uploadInput.files[0]);
    axios
      .post("/upload", data)
      .then((res) => {
        toast.success("Uploaded Successfully");
        console.log(res);
        this.props.closeModal();
      })
      .catch((err) => {
        console.log(err);
      });
  }
  render() {
    return (
      <Modal show={this.props.isOpen} onHide={this.props.closeModal}>
        <Modal.Header closeButton>
          <Modal.Title>Upload the image</Modal.Title>
        </Modal.Header>
        <form onSubmit={this.handleUploadImage}>
          <Modal.Body>
            <Form.Group controlId="formBasicFile">
              <div>
                <input
                  ref={(ref) => {
                    this.uploadInput = ref;
                  }}
                  type="file"
                />
              </div>
              <br />
            </Form.Group>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={this.props.closeModal}>
              Close
            </Button>
            <Button variant="primary" type="submit">
              Upload
            </Button>
          </Modal.Footer>
        </form>
        <Toaster />
      </Modal>
    );
  }
}
