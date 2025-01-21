<template>
    <div>
        <h3>부모 컴포넌트입니다.</h3>
        이름을 입력하세요: <input v-model="dynamicMsg">
        <hr>
        <ParentChild @update-name="updateName" @some-event="someCallback" @emit-args="getNumber"
            my-msg="message" :dynamic-msg="dynamicMsg"/>
    </div>
</template>

<script setup>
    import ParentChild from './ParentChild.vue';
    import {ref} from 'vue'
    const dynamicMsg = ref("d-message")

    const someCallback = function(){
        console.log("어떠한 이벤트가 발생했습니다.")
    }

    const getNumber = function(...args){
        console.log(args)
    }

    const updateName = function(arg){
        dynamicMsg.value = arg
    }
</script>

<style scoped>

</style>