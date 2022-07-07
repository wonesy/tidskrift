CREATE MIGRATION m1ybippyxbssi7tgih3mwi2ytxcu6gnjalggos3yadmlmsscivaigq
    ONTO m1qntcyhaeq3d6yswosr2jranyfd3h2i33gwd2wqvlf2k7a3r6ricq
{
  CREATE TYPE default::Genre {
      CREATE REQUIRED PROPERTY name -> std::str {
          CREATE CONSTRAINT std::exclusive;
          CREATE CONSTRAINT std::min_len_value(2);
      };
  };
  CREATE TYPE default::Book {
      CREATE MULTI LINK genres -> default::Genre;
      CREATE REQUIRED PROPERTY author -> std::str;
      CREATE REQUIRED PROPERTY external_id -> std::uuid {
          SET default := (std::uuid_generate_v1mc());
          SET readonly := true;
      };
      CREATE PROPERTY image_url -> std::str;
      CREATE REQUIRED PROPERTY title -> std::str;
  };
  CREATE TYPE default::BookChoice {
      CREATE REQUIRED LINK book -> default::Book;
      CREATE REQUIRED LINK club -> default::Club;
      CREATE REQUIRED LINK host -> default::User;
      CREATE REQUIRED PROPERTY due_by -> std::datetime;
      CREATE REQUIRED PROPERTY external_id -> std::uuid {
          SET default := (std::uuid_generate_v1mc());
          SET readonly := true;
      };
  };
  CREATE TYPE default::Completion {
      CREATE REQUIRED LINK book_choice -> default::BookChoice;
      CREATE REQUIRED LINK reader -> default::User;
      CREATE REQUIRED PROPERTY completed_at -> std::datetime {
          SET default := (std::datetime_current());
      };
      CREATE PROPERTY rating -> std::float32 {
          CREATE CONSTRAINT std::max_value(10);
          CREATE CONSTRAINT std::min_value(0);
      };
      CREATE PROPERTY will_not_finish -> std::bool {
          SET default := false;
      };
  };
  CREATE TYPE default::Invitation {
      CREATE REQUIRED LINK club -> default::Club;
      CREATE REQUIRED LINK sponsor -> default::User;
      CREATE REQUIRED PROPERTY expires_at -> std::datetime {
          SET default := ((std::datetime_current() + <std::duration>'72 hours'));
      };
      CREATE REQUIRED PROPERTY invitation_id -> std::uuid {
          SET default := (std::uuid_generate_v1mc());
          SET readonly := true;
      };
  };
};
