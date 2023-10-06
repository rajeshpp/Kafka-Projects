rsconf = {
  _id: "rs1",
  members: [{ _id: 0, host: "mongo1"}]
};
rs.initiate(rsconf);
rs.status();
