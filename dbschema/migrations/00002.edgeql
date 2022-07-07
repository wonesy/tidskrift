CREATE MIGRATION m1qntcyhaeq3d6yswosr2jranyfd3h2i33gwd2wqvlf2k7a3r6ricq
    ONTO m16mllhq3lgjuh6wfglo7355jibrw7zixeki63by3zzsdgpuuxx3oa
{
  CREATE TYPE default::Club {
      CREATE REQUIRED LINK creator -> default::User;
      CREATE MULTI LINK members -> default::User;
      CREATE REQUIRED PROPERTY external_id -> std::uuid {
          SET default := (std::uuid_generate_v1mc());
          SET readonly := true;
      };
      CREATE REQUIRED PROPERTY name -> std::str {
          CREATE CONSTRAINT std::min_len_value(8);
      };
  };
  ALTER TYPE default::User {
      CREATE MULTI LINK clubs := (.<members[IS default::Club]);
  };
};
