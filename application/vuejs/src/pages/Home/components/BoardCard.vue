<template>
  <router-link :to="boardUrl">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{ title }}</h5>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: 'BoardCard',
  props: {
    title: {
      type: String,
      default: '',
    },
    boardId: {
      type: Number,
      default: null,
    },
  },
  computed: {
    boardUrl() {
      return `/boards/${this.boardId}`;
    },
  },
};
</script>