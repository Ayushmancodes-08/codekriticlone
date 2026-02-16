import React from 'react';
import './SkeletonLoader.css';

const SkeletonLoader = ({ type = 'dashboard' }) => {
    return (
        <div className="skeleton-overlay">
            <div className="skeleton-container">
                {type === 'dashboard' && (
                    <>
                        {/* Header Skeleton */}
                        <div className="skeleton-header">
                            <div className="skeleton-logo skeleton-shimmer"></div>
                            <div className="skeleton-nav">
                                <div className="skeleton-nav-item skeleton-shimmer"></div>
                                <div className="skeleton-nav-item skeleton-shimmer"></div>
                                <div className="skeleton-nav-item skeleton-shimmer"></div>
                            </div>
                        </div>

                        {/* Main Content Skeleton */}
                        <div className="skeleton-content">
                            {/* Title */}
                            <div className="skeleton-title skeleton-shimmer"></div>

                            {/* Cards Grid */}
                            <div className="skeleton-cards-grid">
                                {[1, 2, 3].map((i) => (
                                    <div key={i} className="skeleton-card">
                                        <div className="skeleton-card-header skeleton-shimmer"></div>
                                        <div className="skeleton-card-body">
                                            <div className="skeleton-text skeleton-shimmer"></div>
                                            <div className="skeleton-text skeleton-shimmer" style={{ width: '80%' }}></div>
                                            <div className="skeleton-text skeleton-shimmer" style={{ width: '60%' }}></div>
                                        </div>
                                    </div>
                                ))}
                            </div>

                            {/* Table Skeleton */}
                            <div className="skeleton-table">
                                <div className="skeleton-table-header skeleton-shimmer"></div>
                                {[1, 2, 3, 4].map((i) => (
                                    <div key={i} className="skeleton-table-row">
                                        <div className="skeleton-table-cell skeleton-shimmer"></div>
                                        <div className="skeleton-table-cell skeleton-shimmer"></div>
                                        <div className="skeleton-table-cell skeleton-shimmer"></div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </>
                )}

                {type === 'login' && (
                    <div className="skeleton-login">
                        <div className="skeleton-login-box">
                            <div className="skeleton-title skeleton-shimmer" style={{ margin: '0 auto 2rem' }}></div>
                            <div className="skeleton-input skeleton-shimmer"></div>
                            <div className="skeleton-input skeleton-shimmer"></div>
                            <div className="skeleton-button skeleton-shimmer"></div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default SkeletonLoader;
