const keyValueDb = process.env.KEY_VALUE_DB;
const user = process.env.KEY_VALUE_USER;
const password = process.env.KEY_VALUE_PASSWORD;

print("Initializing key-value DB user");

const dbInstance = db.getSiblingDB(keyValueDb);

dbInstance.createUser({
  user: user,
  pwd: password,
  roles: [
    {
      role: "readWrite",
      db: keyValueDb
    }
  ]
});