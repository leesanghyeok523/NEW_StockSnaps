<template>
    <div class="exchange-rates">
      <h1>환율 계산기</h1>
      <div class="calculation-container">
        <!-- 환율 계산 옵션 -->
        <div class="rate-options">
          <label>
            <input type="radio" v-model="rateType" value="기준환율" /> 외화 기준
          </label>
          <label>
            <input type="radio" v-model="rateType" value="현찰환율" /> 현찰 기준
          </label>
        </div>
  
        <!-- 통화 선택 -->
        <CurrencySelector :currencies="currencies" v-model="selectedCurrency" />
  
        <!-- 환율 입력 -->
        <RateInput v-model:amount="amount" @calculate="handleCalculate" />
  
        <!-- 결과 출력 -->
        <div class="result" v-if="convertedAmount !== null">
          <p>환전 결과: <strong>{{ convertedAmount }}</strong> {{ selectedCurrency }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  // 환율 계산기 메인 페이지
  import { ref, computed } from 'vue';
  import CurrencySelector from './CurrencySelector.vue';
  import RateInput from './RateInput.vue';
  import { useExchangeRatesStore } from '@/stores/exchangeRates';
  
  export default {
    components: { CurrencySelector, RateInput },
    setup() {
      const rateType = ref('기준환율');
      const amount = ref(0);
      const selectedCurrency = ref('USD');
      const store = useExchangeRatesStore();
  
      // 환전 결과 계산
      const convertedAmount = computed(() => {
        const rate = store.getRate(selectedCurrency.value, rateType.value);
        return rate ? amount.value * rate : null;
      });
  
      const handleCalculate = () => {
        store.fetchRates(); // 최신 환율 정보 가져오기
      };
  
      return { rateType, amount, selectedCurrency, convertedAmount, handleCalculate };
    },
  };
  </script>
  
  <style scoped>
  .exchange-rates {
    padding: 20px;
    background: #f9f9f9;
    border-radius: 8px;
    max-width: 600px;
    margin: 0 auto;
  }
  
  .calculation-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .result {
    padding: 10px;
    background: #e3f2fd;
    border-radius: 5px;
  }
  </style>
  