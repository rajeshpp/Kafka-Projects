rsconf = {
  _id: "rs2",
  members: [{ _id: 0, host: "mongo2"}]
};
rs.initiate(rsconf);
rs.status();
