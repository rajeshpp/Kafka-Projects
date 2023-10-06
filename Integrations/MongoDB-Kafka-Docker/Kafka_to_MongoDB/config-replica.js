rsconf = {
  _id: "ReplicationSet",
  members: [{ _id: 0, host: "mongo1"},
            { _id: 1, host: "mongo2"},
            { _id: 2, host: "mongo3"}]
};
rs.initiate(rsconf);
rs.status();
