<template>
    <div>
        <h5>손자 컴포넌트입니다.</h5>
        <p>{{myMsg}}</p>
        <p>{{dynamicMsg}}</p>
        <input type="text" v-model="name">
        <button @click="updateName">이름 변경 요청</button>
        <hr>
    </div>
</template>

<script setup>
    import {ref} from 'vue'
    const props = defineProps({
        myMsg : String,
        dynamicMsg : String
    })
    const name = ref("")
    const emit = defineEmits(['updateName'])
    const updateName = function(){
        emit("updateName", name.value)
    }
</script>

<style scoped>

</style>