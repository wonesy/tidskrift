CREATE MIGRATION m15z7o6oqx5hwphkhjbkqlf3nox7wgm3yke52vh45gp3vufs4h2xgq
    ONTO m1ybippyxbssi7tgih3mwi2ytxcu6gnjalggos3yadmlmsscivaigq
{
  ALTER TYPE default::Club {
      ALTER LINK members {
          ON TARGET DELETE  ALLOW;
      };
  };
  ALTER TYPE default::User {
      ALTER PROPERTY username {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
