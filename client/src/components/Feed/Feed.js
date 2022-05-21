import React from "react";
import Upload from "../Upload/Upload";
import { useState, useEffect } from "react";
import axios from "../../utils/axios";
// import bootstrap crads
import { Card, CardImg } from "reactstrap";

export default function Feed() {
  const [posts, setPosts] = useState([]);

  const getPosts = async () => {
    const res = await axios.get("/posts");
    console.log(res.data);
    setPosts(res.data);
  };
  const baseURL = "http://127.0.0.1:5000/static";

  useEffect(() => {
    getPosts();
    console.log(posts);
  }, []);

  return (
    <>
      <Upload />
      {/* show images  */}
      <div className="container">
        <div className="row">
          {posts.posts &&
            posts.posts.map((post) => (
              <div className="col-md-4">
                <Card>
                  <CardImg
                    top
                    width="100%"
                    src={baseURL + post.image_url}
                    alt="Card image cap"
                  />
                </Card>
              </div>
            ))}
        </div>
      </div>
    </>
  );
}
