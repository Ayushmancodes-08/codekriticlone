import React, { useState, useEffect } from 'react';
import { useGlobalLoading } from '@/hooks/useGlobalLoading';
import Loader from '@/components/Loader';

const GlobalLoader = () => {
    const isLoading = useGlobalLoading();
    const [showLoader, setShowLoader] = useState(false);

    useEffect(() => {
        if (isLoading) {
            setShowLoader(true);

            // Auto-hide loader after 6 seconds maximum
            const timeout = setTimeout(() => {
                setShowLoader(false);
            }, 6000); // 6 seconds max

            return () => clearTimeout(timeout);
        } else {
            setShowLoader(false);
        }
    }, [isLoading]);

    if (!showLoader) return null;

    return (
        <Loader
            message="Loading... Please wait (max 6 seconds)"
            fullScreen={true}
        />
    );
};

export default GlobalLoader;
