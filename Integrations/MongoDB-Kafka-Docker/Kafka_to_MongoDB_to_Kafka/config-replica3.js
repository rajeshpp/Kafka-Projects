rsconf = {
  _id: "rs3",
  members: [{ _id: 0, host: "mongo3"}]
};
rs.initiate(rsconf);
rs.status();
