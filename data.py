state_transitions = {
    "idle": [
        "startup",
        "crouch",
        "walking",
        "jump",
        "hitstun",
        "airborne"
    ],

    "jump": [
        "airborne",
        "hitstun",
    ],

    "airborne": [
        "landing",
        "startup",
        "air_attack_start_up",
        "air_hitstun",

    ],

    "air_hitstun": [
        "dead",
        "airborne",
        "landing",
    ],

    "air_attack_start_up": [
        "air_active",
        "air_hitstun",
    ],

    "air_active": [
        "air_recovery",
        "air_hitstun",
    ],

    "air_recovery": [
        "air_attack_start_up",
        "landing",
        "airborne",
        "air_hitstun",
    ],

    "landing": [
        "idle",
        "walking",
        "crouch",
        "hitstun",
    ],

    "crouch": [
        "idle",
        "crouch_block",
        "startup",
        "hitstun",
        "walking"
    ],

    "crouch_block": [
        "block_stun",
        "hitstun",
        "crouch",
    ],

    "walking": [
        "block",
        "jump",
        "idle",
        "hitstun",
        "startup",
        "crouch",
        "airborne"
    ],

    "startup": [
        "active",
        "hitstun",
    ],

    "active": [
        "recovery",
        "hitstun",
    ],

    "recovery": [
        "startup",
        "idle",
        "hitstun",
        "crouch",
        "airborne"
    ],

    "block": [
        "walking",
        "idle",
        "block_stun",
        "hitstun",
    ],

    "block_stun": [
        "idle",
        "hitstun",
    ],

    "hitstun": [
        "idle",
        "dead",
    ],

    "dead": [],
}