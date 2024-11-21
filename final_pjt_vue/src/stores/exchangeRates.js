// 환율 데이터 저장 스토어

import { defineStore } from 'pinia';
import axios from 'axios';

export const useExchangeRatesStore = defineStore('exchangeRates', {
  state: () => ({
    rates: {},
  }),
  actions: {
    async fetchRates() {
      try {
        const response = await axios.get('https://api.exchangerate-api.com/v4/latest/USD');
        this.rates = response.data.rates;
      } catch (error) {
        console.error('환율 데이터를 가져오는 중 오류 발생:', error);
      }
    },
    getRate(currency, type) {
      // 환율 계산 타입에 따른 반환 로직 (기본환율/현찰환율 등 추가)
      return this.rates[currency] || null;
    },
  },
});
