<template>
  <div class="exchange-calculator">
    <h1>외화 환전</h1>
    <div class="form-container">
      <!-- 환전 기준 선택 -->
      <div class="rate-type">
        <label>
          <input type="radio" v-model="rateType" value="기준환율" />
          외화 기준
        </label>
        <label>
          <input type="radio" v-model="rateType" value="현찰환율" />
          현찰 기준
        </label>
      </div>

      <!-- 날짜 선택 -->
      <div class="date-input">
        <label for="date">기준 일시:</label>
        <input type="date" id="date" v-model="selectedDate" />
      </div>

      <!-- 통화 선택 -->
      <CurrencySelector
        :currencies="currencies"
        v-model="selectedCurrency"
      />

      <!-- 환전 금액 입력 -->
      <RateInput v-model="amount" />

      <!-- 환율 계산 결과 -->
      <div class="result">
        <p v-if="convertedAmount !== null">
          환전 결과: 
          <strong>{{ convertedAmount.toFixed(2) }}</strong> 원
        </p>
        <p v-else>환율 데이터를 가져오는 중입니다...</p>
      </div>

      <!-- 계산 버튼 -->
      <button @click="handleCalculate">계산하기</button>
    </div>
  </div>
</template>

<script>
import CurrencySelector from "../components/CurrencySelector.vue";
import RateInput from "../components/RateInput.vue";
import { useExchangeRatesStore } from "@/stores/exchangeRates";
import { ref, computed, onMounted } from "vue";

export default {
  components: { CurrencySelector, RateInput },
  setup() {
    const store = useExchangeRatesStore();
    const rateType = ref("기준환율");
    const selectedDate = ref(new Date().toISOString().substr(0, 10)); // 오늘 날짜
    const selectedCurrency = ref("USD");
    const amount = ref(0);

    // 환전 결과 계산
    const convertedAmount = computed(() => {
      const rate = store.getRate(selectedCurrency.value, rateType.value);
      return rate ? amount.value * rate : null;
    });

    // 계산 버튼 클릭 핸들러
    const handleCalculate = async () => {
      await store.fetchRates(); // 환율 데이터 요청
    };

    onMounted(() => {
      handleCalculate(); // 컴포넌트 로드시 환율 데이터 로드
    });

    return {
      rateType,
      selectedDate,
      selectedCurrency,
      amount,
      convertedAmount,
      handleCalculate,
    };
  },
};
</script>

<style scoped>
/* 전체 컨테이너 스타일 */
.exchange-calculator {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: "Roboto", sans-serif;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

/* 폼 컨테이너 스타일 */
.form-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* 환율 유형 스타일 */
.rate-type {
  display: flex;
  gap: 10px;
  justify-content: space-between;
}

.rate-type label {
  font-size: 1rem;
  font-weight: bold;
  color: #333;
}

/* 날짜 입력 스타일 */
.date-input {
  display: flex;
  align-items: center;
  gap: 10px;
}

.date-input label {
  font-weight: bold;
}

.date-input input {
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

/* 결과 표시 스타일 */
.result {
  padding: 10px;
  background-color: #e3f2fd;
  border-radius: 5px;
  font-size: 1.2rem;
  text-align: center;
}

/* 버튼 스타일 */
button {
  padding: 15px;
  font-size: 1.2rem;
  color: white;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}
</style>
