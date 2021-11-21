<template>
    <div>
        <div>
            <represent-block
            :firstColumn="'Actor Name'"
            :secondColumn="'Movies Amount'"
            :thirdColumn="'Best Genre'"
            :actor="true"
            >
            </represent-block>
        </div>
        <div
        v-for="(actor, index) in actors"
        :key='index'>
            <represent-block
            :firstColumn="actor.actor_name"
            :secondColumn="actor.movies_count"
            :thirdColumn="actor.best_genre ? actor.best_genre : '-'"
            :actor="true"
            >
            </represent-block>
        </div>
    </div>
</template>

<script>

import RepresentBlock from '@/components/RepresentBlock.vue'

export default {
    name: 'actors-representation',
    components: {
        RepresentBlock
    },
    data() {
        return {
            actors: []
        }
    },
    methods: {
        async getActors() {
            this.actors = (await this.$api.info.getActors()).data.results
        }
    },
    beforeMount() {
        this.getActors()
    },
}
</script>
