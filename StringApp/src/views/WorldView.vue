<script setup>
import AuthorsComp from '@/components/AuthorsComp.vue';
import NavComponent from '@/components/NavComponent.vue'
</script>
<template>
   <div class="row">
        <div class="col-12"> 
            <NavComponent></NavComponent>
        </div>
    <div class="col-12 mb-3">
         <AuthorsComp></AuthorsComp>
    </div>
     <div class="col-12 mb-3">
         <AuthorsComp></AuthorsComp>
    </div>
     <div class="col-12 mb-3">
         <AuthorsComp></AuthorsComp>
    </div>
     <div class="col-12 mb-3">
         <AuthorsComp></AuthorsComp>
    </div>
     <div class="col-12 mb-3">
         <AuthorsComp></AuthorsComp>
    </div>
     <div class="col-12 mb-3">
         <AuthorsComp></AuthorsComp>
    </div>
   </div>

</template>
<style scoped>
::-webkit-scrollbar{
    display: none;
}
</style>