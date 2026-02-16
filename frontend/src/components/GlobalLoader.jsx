import React from 'react';
import { useGlobalLoading } from '@/hooks/useGlobalLoading';
import Loader from '@/components/Loader';

const GlobalLoader = () => {
    const isLoading = useGlobalLoading();

    if (!isLoading) return null;

    return (
        <Loader
            message="Loading... If this is your first request, the server might be waking up (5-10 seconds)"
            fullScreen={true}
        />
    );
};

export default GlobalLoader;
