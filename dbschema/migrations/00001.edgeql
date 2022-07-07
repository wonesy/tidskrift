CREATE MIGRATION m16mllhq3lgjuh6wfglo7355jibrw7zixeki63by3zzsdgpuuxx3oa
    ONTO initial
{
  CREATE EXTENSION graphql VERSION '1.0';
  CREATE TYPE default::User {
      CREATE PROPERTY created_at -> std::datetime {
          SET default := (std::datetime_current());
      };
      CREATE PROPERTY email -> std::str;
      CREATE REQUIRED PROPERTY external_id -> std::uuid {
          SET default := (std::uuid_generate_v1mc());
          SET readonly := true;
      };
      CREATE PROPERTY first_name -> std::str;
      CREATE PROPERTY last_login_at -> std::datetime;
      CREATE PROPERTY last_name -> std::str;
      CREATE REQUIRED PROPERTY password -> std::str;
      CREATE REQUIRED PROPERTY username -> std::str;
  };
};
