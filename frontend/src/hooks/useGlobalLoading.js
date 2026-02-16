import { useState, useEffect } from 'react';
import { onLoadingChange } from '@/utils/api';

export const useGlobalLoading = () => {
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        const unsubscribe = onLoadingChange(setIsLoading);
        return unsubscribe;
    }, []);

    return isLoading;
};
