<template>
    <div>
        <h4>자식 컴포넌트 입니다.</h4>
        <p>{{ myMsg }}</p>
        <button @click="$emit('someEvent')">자식에 있는 버튼입니다.</button>
        <button @click="buttonClick">자식에 있는 버튼입니다.2</button>
        <button @click="emitArgs">추가 인자 전달</button>
        <hr>
        <ParentGrandChild @update-name="updateName"
            :my-msg="myMsg" :dynamic-msg="dynamicMsg"/>
    </div>
</template>

<script setup>
    import ParentGrandChild from './ParentGrandChild.vue';

    //부모로부터 받은 props를 사용하기 위한 방법은 크게 2가지
    // defineProps(['myMsg']) // 너무나도 심플한 받기

    // 적어도 타입 정도는 알려줘 더 자세히 써주면 좋고
    defineProps({
        myMsg: String,
        dynamicMsg : String
    })
    const emit = defineEmits(["someEvent", "emitArgs", "updateName"])
    const buttonClick = function(){
        emit("someEvent")
    }
    const emitArgs = function(){
        emit("emitArgs", 1, 2, 3)
    }
    const updateName = function(arg){
        emit("updateName", arg)
    }
</script>

<style scoped>

</style>