<template>
    <div>
        <h3>Board View</h3>
        <RouterLink to="/board">게시글 목록</RouterLink> | 
        <RouterLink :to="{name: 'boardList'}">게시글목록 Name</RouterLink> | 
        <RouterLink to="/board/create">게시글 등록</RouterLink> | 
        <RouterLink :to="{name: 'boardCreate'}">게시글등록 Name</RouterLink>
        <hr>
        <RouterView />
    </div>
</template>

<script setup>

</script>

<style scoped>

</style>