<template>
    <button>
        <slot></slot>
    </button>
</template>

<style scoped>
    button {
        display: block;
        background: linear-gradient(47.94deg, #2C3341 19.6%, #313949 77.32%);
        border: 2px solid rgba(49, 57, 73, 0.5);
        box-sizing: border-box;
        box-shadow: -10px -10px 20px rgba(72, 80, 99, 0.26), 10px 10px 20px #262C37;
        border-radius: 12px;
        font-size: 22px;
        font-weight: 700;
        color: rgba(255, 255, 255, 0.65);
        line-height: 27px;
        margin: 18px auto;
        text-align: center;
        padding: 12px 0px;
        width: 360px;
        transition: 0.3s;
        -o-transition: 0.3s ease-in-out;
        -moz-transition: 0.3s ease-in-out;
        -webkit-transition: 0.3s ease-in-out;
    }

    button:hover {
        box-shadow: -10px -10px 20px 4px rgba(72, 80, 99, 0.26), 10px 10px 20px 8px #262C37;
        transition: 0.3s;
        -o-transition: 0.3s ease-in-out;
        -moz-transition: 0.3s ease-in-out;
        -webkit-transition: 0.3s ease-in-out;
    }

    button:active {
        box-shadow: inset -5px -5px 10px rgba(64, 75, 95, 0.25), inset 5px 5px 10px #2C3341, -10px -10px 20px 4px rgba(72, 80, 99, 0.26), 10px 10px 20px 8px #262C37;
    }
</style>