import { View, Text } from "react-native";
import React from "react";
import styles from "../styles/global";
import { useEffect, useState } from "react";
import axios from "axios";

// Set the default values for axios
axios.defaults.withCredentials = true;
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export default function index() {
  const [username, setUsername] = useState();
  const [error, setError] = useState("");

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/user/")
      .then((res) => {
        setUsername(res.data.user.username);
      })
      .catch((err) => {
        setError(err.message);
      });
  }),
    [];

  return (
    <View style={styles.mainContainer}>
      {username ? (
        <Text style={styles.title}>Hello {username}</Text>
      ) : (
        <Text style={styles.title}>Hello World</Text>
      )}
    </View>
  );
}
