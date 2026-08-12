state_transitions = {
    "idle": [
        "startup",
        "crouch",
        "walking",
        "jump",
        "hitstun",
    ],

    "jump": [
        "airborne",
        "hitstun",
    ],

    "airborne": [
        "landing",
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
        "hitstun",
    ],

    "crouch": [
        "idle",
        "crouch_block",
        "startup",
        "hitstun",
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