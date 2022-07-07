using extension graphql;

module default {
    type User {
        required property external_id -> uuid {
            readonly := true;
            default := uuid_generate_v1mc();
        };
        required property username -> str {
            constraint exclusive;
        };
        required property password -> str;
        property first_name -> str;
        property last_name -> str;
        property email -> str;
        property created_at -> datetime {
            default := datetime_current();
        };
        property last_login_at -> datetime;
        multi link clubs := .<members[is Club]
    }

    type Club {
        required property external_id -> uuid {
            readonly := true;
            default := uuid_generate_v1mc();
        };
        required property name -> str {
            constraint min_len_value(8);
        };
        required link creator -> User;
        multi link members -> User {
            on target delete allow;
        };
    }

    type Book {
        required property external_id -> uuid {
            readonly := true;
            default := uuid_generate_v1mc();
        };
        required property title -> str;
        required property author -> str;
        multi link genres -> Genre;
        property image_url -> str;
    }

    type Genre {
        required property name -> str {
            constraint exclusive;
            constraint min_len_value(2);
        }
    }

    type BookChoice {
        required property external_id -> uuid {
            readonly := true;
            default := uuid_generate_v1mc();
        };
        required link club -> Club;
        required link book -> Book;
        required link host -> User;
        required property due_by -> datetime;
    }

    type Completion {
        required link book_choice -> BookChoice;
        required link reader -> User;
        required property completed_at -> datetime {
            default := datetime_current();
        };
        property rating -> float32 {
            constraint min_value(0);
            constraint max_value(10);
        };
        property will_not_finish -> bool {
            default := false;
        }
    }

    type Invitation {
        required property invitation_id -> uuid {
            readonly := true;
            default := uuid_generate_v1mc();
        };
        required link sponsor -> User;
        required link club -> Club;
        required property expires_at -> datetime {
            default := datetime_current() + <duration>'72 hours';
        };
    }
}