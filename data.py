state_transitions = {
    "idle": [
        "attack_start_up",
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
        "attack_start_up",
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
        "attack_start_up",
        "crouch",
    ],

    "attack_start_up": [
        "attack_active",
        "hitstun",
    ],

    "attack_active": [
        "attack_recovery",
        "hitstun",
    ],

    "attack_recovery": [
        "attack_start_up",
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