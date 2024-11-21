<!-- <template>
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

    const savings = computed(() => {
      const result = JSON.parse(JSON.stringify(savingsStore.savings));
      console.log('Savings in Computed:', result); // 여기에서 확인
      return result;
    });

    const loadSavingsData = async () => {
      try {
        await savingsStore.fetchSavingsData();
        console.log('Savings after fetch:', savingsStore.savings); // 데이터가 fetch 후 어떻게 들어오는지 확인
      } catch (error) {
        alert('예적금 데이터를 불러오는 데 실패했습니다.');
        console.error(error.message || error);
      }
    };

    onMounted(() => {
      console.log('Savings before fetch:', savingsStore.savings); // fetch 전에 초기 상태 확인
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
</style> -->


<template>
  <div class="savings-comparison-page">
    <h1>예적금 비교</h1>
    <p>다양한 예적금 상품을 비교해 보세요.</p>

    <!-- 필터 버튼 -->
    <div class="filter-buttons">
      <button :class="{ active: selectedType === 'deposit' }" @click="setType('deposit')">예금</button>
      <button :class="{ active: selectedType === 'saving' }" @click="setType('saving')">적금</button>
    </div>

    <!-- 필터링된 데이터 테이블 -->
    <SavingsTable :savings="filteredProducts" />

    <p v-if="filteredProducts.length === 0" class="loading">데이터를 불러오는 중...</p>
  </div>
</template>

<script>
import { useSavingsStore } from "@/stores/savings";
import { ref, computed, onMounted } from "vue";
import SavingsTable from "@/components/SavingsTable.vue";

export default {
  components: { SavingsTable },
  setup() {
    const savingsStore = useSavingsStore();
    const selectedType = ref("saving"); // 기본값: 적금

    // 선택된 타입에 따라 필터링된 데이터를 계산
    const filteredProducts = computed(() => {
      if (selectedType.value === "deposit") {
        return savingsStore.deposits; // 예금 데이터
      } else if (selectedType.value === "saving") {
        return savingsStore.savings; // 적금 데이터
      }
      return [];
    });

    const setType = (type) => {
      selectedType.value = type;
    };

    const loadSavingsData = async () => {
      try {
        console.log("Fetching savings and deposit data...");
        await savingsStore.fetchSavingsData();
      } catch (error) {
        console.error("데이터를 불러오는 데 실패했습니다:", error);
        alert("데이터를 불러오는 데 실패했습니다.");
      }
    };

    onMounted(() => {
      loadSavingsData();
    });

    return {
      filteredProducts,
      selectedType,
      setType,
    };
  },
};
</script>



<style scoped>
.savings-comparison-page {
  text-align: center;
  padding: 20px;
  font-family: 'Roboto', sans-serif;
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

.filter-buttons {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 20px;
}

.filter-buttons button {
  padding: 10px 20px;
  font-size: 1rem;
  color: white;
  background: #007bff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.filter-buttons button.active {
  background: #0056b3;
  font-weight: bold;
}

.filter-buttons button:hover {
  background: #0056b3;
}

.loading {
  font-size: 1.2rem;
  color: #999;
  font-style: italic;
}
</style>




