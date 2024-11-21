<template>
  <div class="savings-comparison-page">
    <h1>예적금 비교</h1>
    <p>다양한 예적금 상품을 비교해 보세요.</p>
    <SavingsTable :savings="savings" />
    <p v-if="savings.length === 0" class="loading">저축 상품 데이터를 불러오는 중...</p>
  </div>
</template>

<script>
import { useSavingsStore } from '@/stores/savings';
import { onMounted, computed } from 'vue';
import SavingsTable from '@/components/SavingsTable.vue';

export default {
  components: { SavingsTable },
  setup() {
    const savingsStore = useSavingsStore();

    // Proxy 객체를 일반 배열로 변환
    const savings = computed(() => {
      return JSON.parse(JSON.stringify(savingsStore.savings));
    });

    const loadSavingsData = async () => {
      try {
        await savingsStore.fetchSavingsData();
      } catch (error) {
        alert('예적금 데이터를 불러오는 데 실패했습니다.');
        console.error(error.message || error);
      }
    };

    onMounted(() => {
      loadSavingsData();
    });

    return {
      savings,
    };
  },
};
</script>

<style scoped>
.savings-comparison-page {
  text-align: center;
  padding: 20px;
  font-family: "Roboto", sans-serif;
}

h1 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 10px;
}

p {
  font-size: 1rem;
  color: #666;
  margin-bottom: 20px;
}

.loading {
  font-size: 1.2rem;
  color: #999;
  font-style: italic;
}
</style>
